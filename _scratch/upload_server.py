"""Local upload sink: serves an uploader page; saves POSTed files to _scratch/captures."""
import http.server, os, urllib.parse

OUTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "captures")
os.makedirs(OUTDIR, exist_ok=True)

PAGE = b"""<!DOCTYPE html><html><body style="font:16px sans-serif">
<h3 id="status">Relay ready: postMessage {name, text} or choose a file.</h3>
<input type="file" id="f">
<script>
window.addEventListener('message', async (e) => {
  try {
    const {name, text} = e.data || {};
    if (!name || text === undefined) return;
    const r = await fetch('/save?name=' + encodeURIComponent(name), {method: 'POST', body: text});
    const saved = await r.text();
    document.getElementById('status').textContent = 'saved: ' + saved;
    if (e.source) e.source.postMessage({saved: saved, name: name}, '*');
  } catch (err) {
    document.getElementById('status').textContent = 'error: ' + err.message;
    if (e.source) e.source.postMessage({error: String(err), name: (e.data||{}).name}, '*');
  }
});
document.getElementById('f').addEventListener('change', async (e) => {
  const file = e.target.files[0];
  if (!file) return;
  const buf = await file.arrayBuffer();
  const r = await fetch('/save?name=' + encodeURIComponent(file.name), {method: 'POST', body: buf});
  document.getElementById('status').textContent = 'saved: ' + await r.text();
});
</script></body></html>"""

class H(http.server.BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self._cors()
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(PAGE)))
        self.end_headers()
        self.wfile.write(PAGE)

    def do_POST(self):
        q = urllib.parse.urlparse(self.path).query
        name = urllib.parse.parse_qs(q).get("name", ["capture.png"])[0]
        name = os.path.basename(name)
        n = int(self.headers.get("Content-Length", 0))
        data = self.rfile.read(n)
        path = os.path.join(OUTDIR, name)
        with open(path, "wb") as f:
            f.write(data)
        body = path.encode()
        self.send_response(200)
        self._cors()
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass

http.server.ThreadingHTTPServer(("127.0.0.1", 8123), H).serve_forever()

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse, HTMLResponse

from src.config import ASSETS_DIR


IMAGE_EXTENSIONS = {".avif", ".gif", ".jpeg", ".jpg", ".png", ".webp"}

app = FastAPI(title="Image Grid Experiment")


def _safe_asset_path(relative_path: str = "") -> Path:
    path = (ASSETS_DIR / relative_path).resolve()
    assets_root = ASSETS_DIR.resolve()

    if path != assets_root and assets_root not in path.parents:
        raise HTTPException(status_code=400, detail="Path must stay inside assets")

    return path


def _asset_relative_path(path: Path) -> str:
    return path.resolve().relative_to(ASSETS_DIR.resolve()).as_posix()


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return HTML


@app.get("/api/directories")
def list_directories() -> dict[str, list[str]]:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    directories = sorted(
        _asset_relative_path(path)
        for path in ASSETS_DIR.iterdir()
        if path.is_dir()
    )

    return {"directories": directories}


@app.get("/api/images")
def list_images(directory: str = Query("", alias="dir")) -> dict[str, object]:
    selected_dir = _safe_asset_path(directory)

    if not selected_dir.exists():
        raise HTTPException(status_code=404, detail="Directory does not exist")

    if not selected_dir.is_dir():
        raise HTTPException(status_code=400, detail="Selected path is not a directory")

    images = []
    for path in sorted(selected_dir.iterdir(), key=lambda item: item.name.lower()):
        if not path.is_file() or path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        stat = path.stat()
        relative_path = _asset_relative_path(path)
        images.append(
            {
                "name": path.name,
                "url": f"/assets/{relative_path}?v={stat.st_mtime_ns}",
                "modified": stat.st_mtime,
            }
        )

    return {"directory": _asset_relative_path(selected_dir), "images": images}


@app.get("/assets/{asset_path:path}")
def serve_asset(asset_path: str) -> FileResponse:
    path = _safe_asset_path(asset_path)

    if not path.exists() or not path.is_file():
        raise HTTPException(status_code=404, detail="Asset not found")

    if path.suffix.lower() not in IMAGE_EXTENSIONS:
        raise HTTPException(status_code=404, detail="Asset not found")

    return FileResponse(path)


HTML = r"""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Image Grid</title>
    <style>
      :root {
        color-scheme: dark;
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background: #101114;
        color: #f2f2f2;
      }

      * {
        box-sizing: border-box;
      }

      body {
        margin: 0;
        min-height: 100vh;
        background:
          radial-gradient(circle at top left, rgba(126, 87, 194, 0.22), transparent 34rem),
          #101114;
      }

      main {
        width: min(1480px, calc(100% - 32px));
        margin: 0 auto;
        padding: 28px 0 40px;
      }

      header {
        display: grid;
        gap: 18px;
        grid-template-columns: 1fr auto;
        align-items: end;
        margin-bottom: 24px;
      }

      h1 {
        margin: 0 0 6px;
        font-size: clamp(2rem, 5vw, 4.5rem);
        line-height: 0.95;
        letter-spacing: -0.07em;
      }

      p {
        margin: 0;
        color: #b8bac4;
      }

      .controls {
        display: flex;
        gap: 8px;
        align-items: center;
        justify-content: flex-end;
        flex-wrap: wrap;
      }

      input,
      select,
      button {
        border: 1px solid rgba(255, 255, 255, 0.14);
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.08);
        color: #f2f2f2;
        font: inherit;
        min-height: 42px;
        padding: 0 14px;
      }

      input {
        width: min(340px, 100%);
      }

      button {
        cursor: pointer;
        background: #f2f2f2;
        color: #101114;
        font-weight: 700;
      }

      .status {
        display: flex;
        justify-content: space-between;
        gap: 16px;
        margin-bottom: 14px;
        color: #b8bac4;
        font-size: 0.92rem;
      }

      .grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
        gap: 14px;
      }

      .tile {
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 18px;
        background: rgba(255, 255, 255, 0.055);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.24);
      }

      .tile a {
        display: block;
        color: inherit;
        text-decoration: none;
      }

      .tile img {
        display: block;
        width: 100%;
        aspect-ratio: 9 / 16;
        object-fit: cover;
        background: #1a1b20;
      }

      .caption {
        overflow: hidden;
        padding: 10px 12px 12px;
        color: #d8d9df;
        font-size: 0.85rem;
        text-overflow: ellipsis;
        white-space: nowrap;
      }

      .empty {
        border: 1px dashed rgba(255, 255, 255, 0.18);
        border-radius: 18px;
        padding: 42px 18px;
        text-align: center;
        color: #b8bac4;
      }

      @media (max-width: 760px) {
        header {
          grid-template-columns: 1fr;
        }

        .controls {
          justify-content: stretch;
        }

        input,
        select,
        button {
          width: 100%;
        }
      }
    </style>
  </head>
  <body>
    <main>
      <header>
        <div>
          <h1>Image Grid</h1>
          <p>View one assets directory at a time. The grid refreshes automatically.</p>
        </div>
        <form class="controls" id="controls">
          <select id="directorySelect" aria-label="Known assets directories"></select>
          <input id="directoryInput" name="dir" placeholder="assets subdirectory, e.g. generated" autocomplete="off" />
          <button type="submit">Load</button>
        </form>
      </header>

      <div class="status">
        <span id="summary">Loading...</span>
        <span id="updated"></span>
      </div>
      <section class="grid" id="grid"></section>
    </main>

    <script>
      const controls = document.querySelector("#controls");
      const directorySelect = document.querySelector("#directorySelect");
      const directoryInput = document.querySelector("#directoryInput");
      const grid = document.querySelector("#grid");
      const summary = document.querySelector("#summary");
      const updated = document.querySelector("#updated");

      let currentDirectory = new URLSearchParams(window.location.search).get("dir") || "";

      async function loadDirectories() {
        const response = await fetch("/api/directories");
        const data = await response.json();
        const options = ["", ...data.directories];

        directorySelect.innerHTML = options
          .map((directory) => `<option value="${escapeHtml(directory)}">${directory || "assets root"}</option>`)
          .join("");
        directorySelect.value = options.includes(currentDirectory) ? currentDirectory : "";
      }

      async function loadImages() {
        const params = new URLSearchParams({ dir: currentDirectory });
        const response = await fetch(`/api/images?${params}`);

        if (!response.ok) {
          const error = await response.json().catch(() => ({ detail: "Unable to load directory" }));
          grid.innerHTML = `<div class="empty">${escapeHtml(error.detail)}</div>`;
          summary.textContent = currentDirectory ? `assets/${currentDirectory}` : "assets root";
          updated.textContent = "";
          return;
        }

        const data = await response.json();
        const label = data.directory ? `assets/${data.directory}` : "assets root";

        summary.textContent = `${label} · ${data.images.length} image${data.images.length === 1 ? "" : "s"}`;
        updated.textContent = `Updated ${new Date().toLocaleTimeString()}`;
        grid.innerHTML = data.images.length
          ? data.images.map(renderImage).join("")
          : `<div class="empty">No images found in ${escapeHtml(label)}.</div>`;
      }

      function renderImage(image) {
        return `
          <article class="tile">
            <a href="${image.url}" target="_blank" rel="noreferrer">
              <img src="${image.url}" alt="${escapeHtml(image.name)}" loading="lazy" />
              <div class="caption" title="${escapeHtml(image.name)}">${escapeHtml(image.name)}</div>
            </a>
          </article>
        `;
      }

      function setDirectory(directory) {
        currentDirectory = directory.trim().replace(/^assets\/?/, "");
        directoryInput.value = currentDirectory;
        directorySelect.value = [...directorySelect.options].some((option) => option.value === currentDirectory)
          ? currentDirectory
          : "";
        const params = new URLSearchParams();
        if (currentDirectory) params.set("dir", currentDirectory);
        history.replaceState(null, "", `${location.pathname}${params.size ? `?${params}` : ""}`);
        loadImages();
      }

      function escapeHtml(value) {
        return String(value)
          .replaceAll("&", "&amp;")
          .replaceAll("<", "&lt;")
          .replaceAll(">", "&gt;")
          .replaceAll('"', "&quot;")
          .replaceAll("'", "&#039;");
      }

      controls.addEventListener("submit", (event) => {
        event.preventDefault();
        setDirectory(directoryInput.value);
      });

      directorySelect.addEventListener("change", () => setDirectory(directorySelect.value));

      directoryInput.value = currentDirectory;
      loadDirectories().then(loadImages);
      setInterval(loadImages, 3000);
      setInterval(loadDirectories, 10000);
    </script>
  </body>
</html>
"""


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.tools.image_grid_server:app", host="127.0.0.1", port=8000, reload=True)

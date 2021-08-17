# jupyter-book-server-proxy

Tinkering with proxying Jupyter Book using [`jupyter-serverproxy`](https://jupyter-server-proxy.readthedocs.io/).

This template repo provides a simple `jupyter-serverproxy` around a web server that will serve files placed in `jupyter_book_server_proxy/static`.

## Usage

Create your own repo from this template repo, clone it and then:

- add Jupyter Book files (eg created in `_build/html` when running Jupyter Book over a set of notebooks) to `jupyter_book_server_proxy/static`;
- install the package: `pip install --upgrade .`
- restart your notebook server *(? can `jupyter-server-proxy` packages be installed and activated without having to restart the notebook server?)*
- access the book from the classic notebook *New* menu (item: *Jupyter Book*) or the JupyterLab launcher;
- alternatively, access the book directly from: `http://SERVER:PORT/jupyter_book_server_proxy`


My current workflow is:

- place source notebooks, `config.yml` and `toc.yml` files into a `content` directory;
- build the book (`jupyter book build --path-output . content
`);
- copy files to proxy package: `cp -r _build/html/* jupyter_book_server_proxy/static`
- build package (`pip install --upgrade .`)
- restart server

## TO DO

- this should probably be a cookie cutter to let you create multiple book proxy packages;
- ideally it should be possible to run Thebe connected sessions using the server rather than having to launch a Binder session. See this [`executablebooks/sphinx-thebe` related issue](https://github.com/executablebooks/sphinx-thebe/issues/27). *I have manually hacked Jupyter Book HTML and used appropriate `jupyter notebook` startup parameters to successfully execute code from a proxied book on a local server.
- ideally it would be possible to click a *View on server* button in the interactive content *Launch* menu that would open the current page into a notebook on the current server, eg mapping `http://localhost:8888/jupyter_book_server_proxy/Intro.html` to `localhost:8888/PATH/Intro.ipynb`


## Manual Local Thebe Hack

- rewrite Thebe config in HMTL files:

(The original thebe local demo suggests `bootstrap: true` but things seem to have moved on and `requestKernel: true` now seems to be the way to do it.)

```html
<script type="text/x-thebe-config">
{
  requestKernel: true,
  kernelOptions: {
    name: "python3",
    serverSettings: {
      "baseUrl": "http://127.0.0.1:8888",
      "token": "test-secret"
    }
  },
}
</script>
<!--
    <script type="text/x-thebe-config">
    {
        requestKernel: true,
        binderOptions: {
            repo: "ouseful-course-containers/ou-tm112-notebooks",
            ref: "master",
        },
        codeMirrorConfig: {
            theme: "abcdef",
            mode: "python"
        },
        kernelOptions: {
            kernelName: "python3",
            path: "./."
        },
        predefinedOutput: true
    }
    </script>
  -->
```
- run server as: `jupyter notebook --NotebookApp.token=test-secret --NotebookApp.allow_origin='*'`

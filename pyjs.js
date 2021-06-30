var namespace;
var namespace_old;
var def_pyodide_path = './pyodide/';

async function init_python(path = './pyodide/'){
	def_pyodide_path = path;
	await loadPyodide({ indexURL : path });
	namespace = pyodide.globals.get("dict")();
	await pyodide.runPythonAsync(`
		import builtins
		import __main__
		import js
		builtins.input = js.prompt
	`, namespace);
	namespace_old = namespace;
}

function reinit_python(){
	console.log('Now not works, just don\'t know why :(');
	namespace = namespace_old;
}

function py_cmd(command){
	if(!namespace)
		return false;
	pyodide.runPython(command, namespace);
	return true;
}

async function py_cmd_async(command){
	if(!namespace)
		return false;
	await pyodide.runPythonAsync(command, namespace);
	return true;
}

async function make_request(url) {
    return new Promise(function (resolve, reject) {
        let xhr = new XMLHttpRequest();
        xhr.open("GET", url);
        xhr.onload = function () {
            if (this.status >= 200 && this.status < 300) {
                resolve(xhr);
            } else {
                reject({
                    status: this.status,
                    statusText: xhr.statusText
                });
            }
        };
        xhr.onerror = function () {
            reject({
                status: this.status,
                statusText: xhr.statusText
            });
        };
        xhr.send();
    });
}

async function py_exec_script_async(filename){
	const xhttp = await make_request(filename);
	await py_cmd_async(xhttp.response);
}

async function py_exec_script(filename){
	const xhttp = await make_request(filename);
	py_cmd(xhttp.response);
}

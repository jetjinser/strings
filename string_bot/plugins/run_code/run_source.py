import requests

languages_dict = {
    "assembly": "main.asm",
    "ats": "main.dats",
    "bash": "main.sh",
    "c": "main.c",
    "clojure": "main.clj",
    "cobol": "main.cob",
    "coffeescript": "main.coffee",
    "cpp": "main.cpp",
    "crystal": "main.cr",
    "csharp": "main.cs",
    "d": "main.d",
    "elixir": "main.ex",
    "elm": "Main.elm",
    "erlang": "main.erl",
    "fsharp": "main.fs",
    "go": "main.go",
    "groovy": "main.groovy",
    "haskell": "main.hs",
    "idris": "main.idr",
    "java": "Main.java",
    "javascript": "main.js",
    "julia": "main.jl",
    "kotlin": "main.kt",
    "lua": "main.lua",
    "mercury": "main.m",
    "nim": "main.nim",
    "ocaml": "main.ml",
    "perl": "main.pl",
    "perl6": "main.pl6",
    "php": "main.php",
    "plaintext": "main.txt",
    "python": "main.py",
    "ruby": "main.rb",
    "rust": "main.rs",
    "scala": "main.scala",
    "swift": "main.swift",
    "typescript": "main.ts"
}


async def code_run(code, language):
    url = f'https://run.glot.io/languages/{language}/latest'
    header = {'Authorization': 'Token 3e5b03d2-6801-41d3-b354-cd42b49075e6', 'Content-type': 'application/json'}

    data = '''{
  "files": [
    {
      "name": "%s",
      "content": "%s"
    }
  ],
  "stdin":"",
  "command":""
}''' % (languages_dict[language], code.replace('"', '\\"'))
    data = data.encode('utf-8')

    resp = requests.post(url, data=data, headers=header)
    resp = resp.json()
    if resp.get('stdout'):
        msg = resp['stdout']
    elif resp.get('stderr'):
        msg = resp['stderr']
    else:
        msg = '也许是网络错误或别的什么'
        print(resp)

    return msg

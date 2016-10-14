import re


def translate(m):
    # Parse IRC messages. Stolen from muirc (https://github.com/Gawen/muirc)

    IRC_RE = re.compile(r"(:(?P<nick>[^ !@]+)(\!(?P<user>[^ @]+))?(\@(?P<host>[^ ]+))? )?(?P<command>[^ ]+) (?P<params1>([^:]*))(?P<params2>(:.*)?)")
    
    if isinstance(m, str):
        # str -> msg
        m = IRC_RE.match(m.strip())

        if not m:
            return None

        m = m.groupdict()

        m["params"] = m.pop("params1").split()
        if m["params2"]:    m["params"] += [m["params2"][1:]]
        m.pop("params2")

        return m

    else:
        # msg -> str
        def gen():
            if m.get("nick", None):
                yield ":" + m["nick"]
                if m.get("user", None):   yield "!" + m["user"]
                if m.get("host", None):   yield "@" + m["host"]
                yield " "

            yield m["command"]
            
            if m.get("params", None):
                for param in m["params"][:-1]:  yield " " + param

                yield " "
                if " " in m["params"][-1]:  yield ":"
                yield m["params"][-1]

            yield ''

        return "".join(gen())
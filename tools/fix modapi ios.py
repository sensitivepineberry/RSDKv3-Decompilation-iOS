import re
import sys

PATH = "RSDKv3/ModAPI.cpp"

BASEVAR = {
    "Data": "dataPath",
    "Scripts": "scriptPath",
    "Videos": "videosPath",
}

# Matches one of the three near-identical blocks in ScanModFolder, from the
# "char folderTest[4][0x10] = {" line through the matching closing brace of
# the "if (tokenPos >= 0) { ... }" block. Anchored on stable structural text
# only (not exact interior whitespace), and captures the label ("Data",
# "Scripts", or "Videos") plus the indentation of the outer lines so the
# replacement can match indentation exactly.
PATTERN = re.compile(
    r'^([ \t]*)char folderTest\[4\]\[0x10\] = \{\s*'
    r'"([A-Za-z]+)/",'
    r'.*?'
    r'info->fileMap\.insert\(std::pair<std::string, std::string>\(pathLower, modBuf\)\);\n'
    r'\1\}',
    re.DOTALL | re.MULTILINE,
)


def build_replacement(indent, label):
    basevar = BASEVAR[label]
    inner = indent + "    "
    return (
        f'{indent}std::string relStr = fs::relative(data_de.path(), {basevar}).generic_string();\n'
        f'{indent}std::string path    = "{label}/" + relStr;\n'
        f'{indent}std::string modPath(modBuf);\n'
        f'{indent}char pathLower[0x100];\n'
        f'{indent}memset(pathLower, 0, sizeof(char) * 0x100);\n'
        f'{indent}for (int c = 0; c < (int)path.size() && c < 0x100; ++c) {{\n'
        f'{inner}pathLower[c] = tolower(path.c_str()[c]);\n'
        f'{indent}}}\n\n'
        f'{indent}info->fileMap.insert(std::pair<std::string, std::string>(pathLower, modBuf));'
    )


def main():
    with open(PATH) as f:
        src = f.read()

    matches = list(PATTERN.finditer(src))
    if len(matches) != 3:
        labels_found = [m.group(2) for m in matches]
        print(f"Expected 3 matches (Data/Scripts/Videos), found {len(matches)}: {labels_found}", file=sys.stderr)
        sys.exit(1)

    # Replace from the end backwards so earlier match spans stay valid.
    for m in reversed(matches):
        indent, label = m.group(1), m.group(2)
        if label not in BASEVAR:
            print(f"Unrecognized label '{label}' in match, aborting", file=sys.stderr)
            sys.exit(1)
        replacement = build_replacement(indent, label)
        src = src[: m.start()] + replacement + src[m.end():]

    with open(PATH, "w") as f:
        f.write(src)

    print("ModAPI.cpp patched successfully (Data, Scripts, Videos blocks fixed)")


if __name__ == "__main__":
    main()

import vim

varKeys_C = ["int", "double", "char", "void"]
varList = []

vim.command("vnew")
vim.command("wincmd r")
cb = vim.current.buffer

for line in vim.buffers[1]:
    for var in varKeys_C:
        if var in line:
            lineList = line.split()
            if lineList[0] in varKeys_C:
                    varList.append(line)

for var in varList:
    if var not in cb:
        cb.append(var)

vim.command("wincmd w")

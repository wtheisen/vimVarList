import vim

varList_C = ["int", "double", "char"]

vim.command("vnew")
cb = vim.current.buffer

for line in vim.buffers[1]:
    for var in varList_C:
        if var in line:
            cb.append(line)

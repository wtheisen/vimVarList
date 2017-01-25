#searches the code for the variable in question
#William Theisen
import vim
import re

#sets up the two buffers
codeBuffer = vim.buffers[1]
varBuffer = vim.current.buffer

#gets the position of the cursor
currentWindow = vim.current.window
cursorPosition = currentWindow.cursor

#gets the line of the variable we want to search for
cursorLine = cursorPosition[0]

varLine = varBuffer[cursorLine - 1]
varName = re.findall(r"\w+", varLine)
varName = varName[1]
print str(varName)

#searches the code buffer for instances of the variable
vim.command("wincmd w")
#vim.command("1")
vim.command('let @/ = ""')
vim.command("/" + varName)
vim.command("let @/='"+varName+"'")
vim.command("normal n")


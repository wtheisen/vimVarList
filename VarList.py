#vim var list - William Theisen
#   This program keeps track of the variables and functions headers used
#   throughout a program in a sidebar
import vim

#list of key words to check matches against
varKeys = {}
varKeys['c'] = ["int", "double", "char", "void"]
varKeys['cpp'] = ["int", "double", "char", "void", "vector<int>"]
varKeys['py'] = ["="]

#dict of tracked variables in the file and line in the list buffer
varList = {}
varLine = 1

#longest declaration line thus far
longestLine = 1

#creates a new buffer, moves it to the right
vim.command("vnew")
vim.command("wincmd r")

#allows the user to close the list without using !
vim.command("setlocal buftype=nofile")
vim.command("setlocal bufhidden=hide")
vim.command("setlocal noswapfile")

#save the current buffer, window, and cursor position
currentBuffer = vim.current.buffer
currentWindow = vim.current.window
cursorPosition = currentWindow.cursor

#gets the file extension of the code file for syntax highlighting and variable
#   matching
fileName = vim.buffers[1]
fileName = fileName.name
fileName = fileName.split('/')
fileName = fileName[-1]
fileName = fileName.split('.')
fileExt = fileName[1]
fileName = fileName[0]

#iteretes through every line and checks for matches in var list
for line in vim.buffers[1]:
    for var in varKeys[str(fileExt)]:
        if var in line:
            lineList = line.split()
            if str(fileExt) == 'py':
                if lineList[1] in varKeys[str(fileExt)]:
                    varList[str(varLine)] = line
                    varLine += 1
            else:
                if lineList[0] in varKeys[str(fileExt)]:
                    varList[str(varLine)] = line
                    varLine += 1

#if we haven't already recorded the var, put it in the current buffer
#   also check and keep track of the longest line
for key, value in varList.iteritems():
    if value not in currentBuffer:
        if len(value) > longestLine:
            longestLine = len(value)
        currentBuffer.append(value.lstrip())

#resize the buffer to be the size of the longest line, switch to orig buffer
#   turn on syntax highlighting, make the list buffer unmodifiable and name
#   the buffer 'variable_list'
vim.command("vertical resize " + str(longestLine))
vim.command("setlocal syntax="+str(fileExt))
vim.command("file variable_list")
vim.command("setlocal nomodifiable")
vim.command("wincmd w")

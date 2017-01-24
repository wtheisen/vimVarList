#vim var list - William Theisen
#   This program keeps track of the variables and functions headers used
#   throughout a program in a sidebar
import vim

#list of key words to check matches against
varKeys_C = ["int", "double", "char", "void"]

#list of tracked variables in the file
varList = {}
varLine = 1

#longest declaration line thus far
longestLine = 1

#creates a new buffer, moves it to the right, records it as the current buffer
vim.command("vnew")
vim.command("wincmd r")

currentBuffer = vim.current.buffer
currentWindow = vim.current.window
cursorPosition = currentWindow.cursor


#iteretes through every line and checks for matches in var list
for line in vim.buffers[1]:
    for var in varKeys_C:
        if var in line:
            lineList = line.split()
            if lineList[0] in varKeys_C:
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
vim.command("vertical resize " + str(longestLine))
vim.command("wincmd w")

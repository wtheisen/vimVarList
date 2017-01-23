if !has('python')
    finish
endif

function! HelloWorld()
    pyfile helloworld.py
endfunction

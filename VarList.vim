if !has('python')
    finish
endif

function! VarList()
    pyfile VarList.py
endfunction

function! SearchVar()
    pyfile VarSearch.py
endfunction

function! ListenEnter()
    echo "listener triggered"
    map <F9> :call SearchVar()<CR>
endfunction

function! ResetEnter()
    echo "Reset triggered"
endfunction


autocmd BufEnter variable_list :call ListenEnter()
autocmd BufLeave variable_list :call ResetEnter()

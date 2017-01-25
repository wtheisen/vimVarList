if !has('python')
    finish
endif

function! VarList()
    map <ENTER> :call SearchVar()<CR>
    pyfile VarList.py
endfunction

function! SearchVar()
    pyfile VarSearch.py
endfunction

function! ListenEnter()
    echo "listener triggered"
    map <ENTER> :call SearchVar()<CR>
endfunction

function! ResetEnter()
    echo "Reset triggered"
    unmap <ENTER>
endfunction


autocmd BufEnter variable_list :call ListenEnter()
autocmd BufLeave variable_list :call ResetEnter()

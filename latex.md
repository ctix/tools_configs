
##  Latex Configuration on Arch Linux
-----
###  1. Install Texlive 
  yay -S texlive-core texlive-bin texlive-langchinese texlive-latexextra

1.1 test with the Chinese UTF support 

```latex
%  test.tex
\documentclass[UTF8]{ctexart}
\begin{document}

Hello world!  \\
我们的椒上 that 的中文  

% test the one line mathmatics formular
$  \sum_{i=0^n}  $

% test the one line mathmatics formular
\( \sum_{i=0}^{n}f(x)    \)

$$  \sum_{i=0}^{n}f(x)    $$ 
\end{document}

```
  1.2 xelatex test.tex
### 2. SpaceVim setup language latex layers 
   2.1  
      [[layers]]
      name = "lang#latex"

```tex
% \ll  Start/Stop compiling the document
% \lk  Stop the running compilation
% \lv  Open pdf viewer and/or do forward searching with
% \le  Parse the log file for errors and warnings
% \lc  Clean auxiliary files (\lC to also clean pdf files)
```

####  2.2  Support xelatex rendering on save 
**  Note: Be sure to set default engine to the 
        xelatex 
        it can employ the local fontset to rendering the 
        pdf onSave , as it knows as rendering on file changes saved!!

Add the below to the .\autoload\SpaceVim\layers\lang\latex.vim
```vim
  let g:tex_flavor = 'latex'
  let g:vimtex_view_method='zathura'
  let g:vimtex_quickfix_mode=0
  let g:vimtex_compiler_latexmk_engines = {
        \ '_'                : '-xelatex',
        \ 'pdflatex'         : '-pdf',
        \ 'dvipdfex'         : '-pdfdvi',
        \ 'lualatex'         : '-lualatex',
        \ 'xelatex'          : '-xelatex',
        \ 'context (pdftex)' : '-pdf -pdflatex=texexec',
        \ 'context (luatex)' : '-pdf -pdflatex=context',
        \ 'context (xetex)'  : '-pdf -pdflatex=''texexec --xtx''',
        \}

  let g:vimtex_compiler_latexrun_engines = {
        \ '_'                : 'xelatex',
        \ 'pdflatex'         : 'pdflatex',
        \ 'lualatex'         : 'lualatex',
        \ 'xelatex'          : 'xelatex',
        \}

  set conceallevel=0
  " let g:tex_conceal='abdmg'
```


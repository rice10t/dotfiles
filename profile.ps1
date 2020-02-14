# $env:HOMEPATH\Documents\WindowsPowerShell に置く

# Bashっぽい補完
Set-PSReadlineKeyHandler -Key Tab -Function Complete

# coreutils 等を使うためにエイリアスを削除する
Remove-Item alias:cat
Remove-Item alias:curl
Remove-Item alias:cp
Remove-Item alias:echo
Remove-Item alias:ls
# TODO mkdir は Function なのでエイリアスとしては削除できない
# Remove-Item alias:mkdir
Remove-Item alias:mv
Remove-Item alias:pwd
Remove-Item alias:rm
Remove-Item -Force alias:sleep

# memo: Set-Alias では引数つきのエイリアスを設定できないため、function で定義する
function ll {
    ls -l
}

function la {
    ls -al
}
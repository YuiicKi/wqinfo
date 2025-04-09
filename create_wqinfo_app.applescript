tell application "Terminal"
    do script "cd /Users/yuii/CascadeProjects/wqinfo && python3 wqinfo.py; echo '\n按回车键关闭窗口'; read -n 1"
    activate
end tell

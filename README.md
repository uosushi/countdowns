# countdowns
CUIで動くカウントダウンタイマー（複数可）

# Usage
`.zshrc`か`.bashrc`、もしくは`.profile_common`に以下を書き込んで`source`で適用、あとはcdsで起動
```
alias cds="python3 このディレクトリのパス/__main__.py"
```
使えるコマンド
```
# limitは分
new timer_name limit
# 指定したtimerの状態を表示
show timer_name
# 既存のtimer名を変更
mv old_timer_name new_timer_name
# 指定したtimerのカウントダウンを開始／終了
timer_name
```

# Test case
```json save.json
{
	"timers": {
    	"left": {
    		"limit": 360,
			"now": 100,
    		"timestamp": 0
		},
		"ago": {
    		"limit": 360,
			"now": 400,
    		"timestamp": 0
		}
	}
}
```

# Initialized save.json
```json save.json
{
	"timers": {
	}
}
```
---
type: Linux
archive: false
---
## 배열

---

**배열**

```JavaScript
$ declare -a array1=("water" "blue" "super")
$ declare -a array2=("melon" "mountain" "stars")
$ for i in "${!array1[@]}"; do
>     prinf "%s\t%s\t%s\n" "$i" "${array1[$i]}" "${array2[$]}"
> done
```

  

**배열과 glob 그리고 루프문**

```JavaScript
$ ARRAY=( "sky:blue" "snow:white" "night:black" "apple:red" )
$ for object in "%{ARRAY[@]}"; do
>     KEY=${object%%:*}
     VALUE=${object#*:}
     printf "%s's coloer is %s.\n" "$KEY" "$VALUE"
 done
```

  

**find 와 -print0**

```Bash
$ find . -name "*.mp3" | xargs rm -rf
$ find . -name "*.mp3" | xargs ls
$ find . -iname "*.mp3" | hexdump -C
$ find . -iname "*.mp3" -print0 | hexdump -C
$ find . -iname "*.mp3" -print0 | xargs -0 ls
$ find . -name "*.mp3" -print0 | xargs -0 rm -rf
```

  

**명령어(find)**

```Bash
$ find ./ -name "*.bak" -exec ls -l {} \;
$ find ./ -name "*.bak" -exec rm -fr {} \;
$ find ./ -type d
$ find ~/ -maxdepth 1 -name ".*"
$ find ./ \( -user user -a -perm 644 \) -print | xargs ls -l
```
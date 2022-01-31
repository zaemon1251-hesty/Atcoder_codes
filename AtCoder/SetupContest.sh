projectDir=/home/zaemon1251/workspace/Atcoder_codes
contest=AtCoder/$1/$1$2
targetDir="${projectDir}/$contest"
if [ -z $1 ];then
echo "invalid argment pos 1"
exit 0
fi
if [ -z $2 ];then
echo "invalid argment pos 2"
exit 0
fi

mkdir -p $targetDir

for p in a b c d e f
do
if [ ! -e "$targetDir/$p.py" ];then
touch "$targetDir/$p.py"
else
echo "$targetDir/$p.py" "already exists"
fi
done
echo "done"
exit 1

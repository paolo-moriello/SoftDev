egrep '<div class="command".*>.* | <div class="num-votes".*>.*' | sed -r 's/<div.*>(.*)<.*>/\1/g' | awk '{line=$0; getline; if($1>=5)print line;}' | sed 's/^[\t ]*//'


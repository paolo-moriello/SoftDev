egrep 'class="comment"' | sed -r 's/(<[^>]*>)*([^<]*)<.*/\2/g'  | sort | uniq -c | sort -n -r

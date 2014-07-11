FARE_DATA="
turnstile_140531.txt
turnstile_140524.txt
turnstile_140517.txt
turnstile_140510.txt
turnstile_140503.txt
"

for i in $FARE_DATA
do
    echo $i
    curl -O http://web.mta.info/developers/data/nyct/turnstile/$i
done

for dir in $(find . -type d -mindepth 1 -maxdepth 1 | grep -v '^\.*$'); do
    echo "$dir"
    cd "$dir"
    poetry update
    cd ..
done
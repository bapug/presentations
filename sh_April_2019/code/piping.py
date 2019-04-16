from sh import git, ssh, head, tail, wc, sort, grep, du


# Get list of files
grep('*')
# Get sizes of each
du('-hM', grep('*'))
# Sort, numerically
sort(du('-hM', grep('*')), '-n')
# And get the largest
tail(sort(du('-hM', grep('*')), '-n'), '-n' 5)


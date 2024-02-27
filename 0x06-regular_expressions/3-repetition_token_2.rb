#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression,
# matching method
# The regular expression must match the given cases

scanner = ARGV[0]
matcher = scanner.scan(/hbt+n/)
puts matcher.join

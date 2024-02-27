#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression,
# matching method
# The regular expression must match the given cases

scanner = ARGV[0]
matches = scanner.scan(/hbt{2,5}n/)
puts matches.join

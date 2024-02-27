#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression,
# matching method
# The regular expression must match School

scanner = ARGV[0]
matches = scanner.scan(/School/)
puts matches.join

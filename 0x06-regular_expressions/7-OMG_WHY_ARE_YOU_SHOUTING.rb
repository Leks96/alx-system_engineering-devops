#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression,
# matching method
# The regular expression must match capital letters

scanner = ARGV[0]
matcher = scanner.scan(/[A-Z]/)
puts matcher.join

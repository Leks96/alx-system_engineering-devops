#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression,
# matching method
# The regular expression must match a 10 digit phone number

scanner = ARGV[0]
matcher = scanner.scan(/^\d{10}$/)
puts matcher.join

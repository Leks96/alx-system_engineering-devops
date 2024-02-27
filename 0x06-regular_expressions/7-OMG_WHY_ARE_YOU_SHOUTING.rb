#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression,
# matching method
# The regular expression must match capital letters

matcher = ARGV[0].scan(/[A-Z]/).join
puts matcher

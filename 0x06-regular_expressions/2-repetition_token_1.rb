#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression,
# matching method

matcher = ARGV[0].scan(/hb?tn/).join
puts matcher

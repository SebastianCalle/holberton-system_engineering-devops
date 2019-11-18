#!/usr/bin/env ruby

str = ARGV[0]
str1 = str.scan(/hbt{2,4}n/).join
puts str1

#!/usr/bin/env ruby

val = ARGV[0]

m = val.scan(/Holberton/) 

if m then
	m.each do
		|thing|
		print thing
	end
end
puts

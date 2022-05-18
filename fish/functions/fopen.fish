function fopen
	if count $argv > /dev/null
			switch $argv
					case e extern
						open (find "/run/media/$USER/" -type f | fzf)
					case '*'
						open (find "$argv" -type f | fzf)
					end
	else
			open (find -type f | fzf)
	end
end


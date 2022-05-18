function fcd
	if count $argv > /dev/null
			switch $argv
					case e extern
						cd (find "/run/media/$USER/" -type d | fzf)
					case '*'
						cd (find "$argv" -type d | fzf)
					end
	else
			cd (find -type d | fzf)
	end
end


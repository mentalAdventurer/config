function fcd
	if count $argv > /dev/null
			switch $argv
					case e extern
						cd (find -L "/run/media/$USER/" -type d | fzf)
                    case d drive
                        cd (find -L "/mnt/data/" -type d | fzf)
                    case l symlink
                        cd (find -L -type d | fzf)
					case '*'
						cd (find "$argv" -type d | fzf)
					end
	else
			cd (find -type d | fzf)
	end
end


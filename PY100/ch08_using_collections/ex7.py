info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

info_list = info.split(':')

new_info = ('+'.join(info_list))
print(new_info)


info2 = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
info3 = info2.replace(':', '+')
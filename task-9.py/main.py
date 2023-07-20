class Solution:
    def stick(*args, **kwargs) -> str:
        output = ''
        
        for item in [item for item in args if isinstance(item, str)]:
            output = item if output == '' else output + f'#{item}'
        
        return output
# https://www.codegrepper.com/code-examples/ruby/append+to+list+ruby

# accepts has with owner name for each file
# returns hash with array of file names for each owner

def group_by_owners(files)
    # for each value, find all keys with that value, group together in new hash where value is now key,
    # new value is array of old keys
    new_hash = {}
    # add vals to new hash don't repeat
    files.each do |key, value|
        # if we have already added that key
        if new_hash.has_key?(value)
            # add the value
            new_hash[value].push(key) 
        else
            # else, add the key and the value
           new_hash[value] = [key]
        end
    end
    return new_hash
end
  
  files = {
    'Input.txt' => 'Randy',
    'Code.py' => 'Stan',
    'Output.txt' => 'Randy'
  }
 puts group_by_owners(files)
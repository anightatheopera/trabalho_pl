import html

def split():
    with open('example.pug', 'r') as f:
        results = []
        for line in f:
                words = line.strip().split()
                results.append(words)
        print (results)
        return results


def to_html(results:list[dict], x) -> str:
    output = ''
    for line in results:
        output += html.escape(line) + ' '  
    return output


def save_html(output:str, x) -> None:
    with open('results.html', 'w') as f:
        f.write(output)

def main():
    results = split()
    output = to_html(results, 'results.html')
    save_html(output, 'results.html')
    
if __name__ == '__main__':
    main()
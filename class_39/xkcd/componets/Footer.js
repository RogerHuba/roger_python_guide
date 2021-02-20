import Link from 'next/Link'

export default function Footer(props){
    const currentNum = props.comicNum;
    const nums = []

    for(let n = currentNum; n > currentNum - 10; n--){
        nums.push(n)
    }

    return(
        <footer>
            <h2>Previous {nums.length}</h2>
            <ul>
                {nums.map(num => (
                    // <li key={num}>
                        <Link href="/num/[id].js" as={`/num/${num}`} key={num}> 
                            <a>#{num}</a>
                        </Link>
                    // </li>
                ))}
            </ul>
        </footer>
    )
}
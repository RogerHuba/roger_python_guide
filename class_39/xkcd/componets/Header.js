import Link from 'next/link';

export default function Header(props){
    return(
        <header>
            <nav>
                <Link href="/">
                    <a>Home</a>
                </Link>
                <Link href="/about">
                    <a>About</a>
                </Link>
                <style jsx>{`
                    a {
                        margin-right: 15px;
                        color: green;
                    }
                `}
                </style>
            </nav>
        </header>
    )
}
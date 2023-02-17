import Link from 'next/link';

export default function Footer() {
    return (
        <footer className="p-4 text-gray-100 bg-gray-500">
            <nav className="flex items-center space-x-10 justify-left">
                <Link href="/careers">
                    <a className="text-xl" href="careers">Careers</a>
                </Link>
            </nav>
        </footer>
    );
}
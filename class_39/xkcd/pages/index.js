import Header from '../componets/Header'
import Footer from '../componets/Footer'

export default function Home(props) {
  return (
    <div className="App">
      <Header />
      <h1>XKCD</h1>
      <h2>{props.comic.title}</h2>
      <img src={props.comic.img} alt={props.comic.alt} />
      <style jsx>{`
      .hello {
        font: 15px Helvetica, Ariel, sans-serif;
        background: #eee;
        padding: 100px;
        text-align: center;
        transition: 100mx ease-in background;
      }
      .hello:hover {
        background: #ccc;
      }
      `}
      </style>
      <Footer comicNum={props.comic.num} />
    </div>
  )
}

export async function getServerSideProps(context) {
  const response = await fetch('http://xkcd.com/info.0.json');
  const data = await response.json();

  return {
    props: {
      comic: data
    }, // will be passed to the page component as props
  }
}

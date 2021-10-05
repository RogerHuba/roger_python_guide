'use strict'

import Head from 'next/head'
import Link from 'next/link'

import { useState } from 'react'
import { replies } from '../data'

export default function Home() {

  // const [reply, setReply] = useState('Ask Me Anything');
  const [answeredQuestions, setAnsweredQuestions] = useState([]);

  function questionAskedHandler(event){
    event.preventDefault()
    const randomReply = replies[Math.floor(Math.random() * replies.length)];
    
    // setReply(randomReply)
    const answeredQuestion = {
      question: event.target.question.value, 
      reply: randomReply,
      id: answeredQuestions.length,
    }

    // console.log('answeredQuestion', answeredQuestion);

    setAnsweredQuestions([...answeredQuestions, answeredQuestion])
  }

  function getLatestReply(){
    if (answeredQuestions.length === 0) {
      return 'Ask me Anything';
    }
    return answeredQuestions[answeredQuestions.length - 1].reply;
  }

  return (
    <div className="">
      <Head>
        <title>Magic 8 Ball</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="">
        <Header answeredQuestionArray = {answeredQuestions}/>
        <QuestionForm />
        <EightBall latestReply = {getLatestReply()}/>
        <ResponseTable answeredQuestionArray = {answeredQuestions}/>
        <Footer />
      </main>
    </div>
  )

  function Header(props){
    return(
      <header className="flex items-center justify-between p-4 bg-gray-500 text-gray-50">
        <h1>Magic 8 Ball</h1>
        <p>{props.answeredQuestionArray.length} Question Answered</p>
      </header>
    )
  }

  function QuestionForm(){
    return(
      <form onSubmit={questionAskedHandler} className = "flex w-1/2 p-2 mx-auto my-4 bg-gray-200">
        <input name="question" className="flex-auto pl-1" />
        <button className="px-2 py-1 bg-gray-500 test-gray-50">Ask</button>
      </form>

        
    )
  }

  function EightBall(props){
    return(
      <div className="mx-auto my-4 bg-gray-900 rounded-full w-96 h-96">
        <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
          <p className="text-xl text-center">{props.latestReply}</p>
        </div>
      </div>
    )
  }

  function ResponseTable(props){
    // console.log(props.answeredQuestionArray)
    return(
      <table className="w-1/2 mx-auto border-4 border-collapse border-gray-500">
        <thead>
          <tr>
            <th className="pl-2 border border-black">No.</th>
            <th className="pl-2 border border-black">Question</th>
            <th className="pl-2 border border-black">Response</th>
          </tr>
        </thead>
        <tbody>
          {props.answeredQuestionArray.map(item =>(
            <tr className="odd:bg-red-400" key={item.id}>
              <td className="pl-2 border border-black">{item.id}</td>
              <td className="pl-2 border border-black">{item.question}</td>
              <td className="pl-2 border border-black">{item.reply}</td>
            </tr>
          ))}
        </tbody>
      </table>
    )
  }

  function Footer(props){
    return(
      <footer className="p-4 mt-8 bg-gray-500 text-gray-50">
        <nav>
          {/* <a href="careers">Careers</a> */}
          <Link href="/careers">
            <a>Careers</a>
          </Link>
        </nav>
      </footer>
    )
  }
}

import React, { useRef } from 'react';
import Card from './Card';

const Foreground = () => {
    const ref=useRef(null);
    const data=[
        {
            desc:"Jay kumar marksheet",
            filesize:"0.9MB",
            close:true,
            tag:{isOpen:true, tagTitle:"DOWNLOAD NOW ",tagcolor:"green"},
        },
       
        {
            desc: "Anita Sharma report",
            filesize: "1.2MB",
            close: false,
            tag: { isOpen: false, tagTitle: "VIEW REPORT", tagcolor: "blue" },
        },
        {
            desc: "Rahul Verma certificate",
            filesize: "0.5MB",
            close: true,
            tag: { isOpen: true, tagTitle: "GET CERTIFICATE", tagcolor: "red" },
        }
    ]
    return (
        <>
        
        <div ref={ref} className='fixed top-0 left-0 z-[3] w-full h-full  flex gap-10 p-5 flex-wrap'>
                {data.map((item, index) => (
                    <Card key={index} {...item}  reference={ref}/>
                ))}
            </div>
       
        </>
    );
}

export default Foreground;

import React from 'react';
import { FaFileAlt } from "react-icons/fa";
import { GrDownload } from "react-icons/gr";
import { IoCloseCircleOutline } from "react-icons/io5";
import { motion } from "motion/react"

const Card= ( data,reference)=>{
 
  return (
    <motion.div drag dragConstraints={reference} whileHover={{scale:1.03}}   className=' relative w-60 h-70 overflow-hidden rounded-[50px] bg-zinc-900 text-white py-4 px-4 '>
      <FaFileAlt />
      <p>{data.desc}</p>
      <div className='footer absolute bottom-0 w-full  px-8 left-0 '>
         <div className=" flex items-center justify-center gap-2.5 py-3  bottom-0"> 
         <h5 className=''>{data.filesize}</h5>
         <span className='w-5 h-5 bg-zinc-600 rounded-full flex items-center justify-center'>
         {data.close ?<IoCloseCircleOutline/>:  <GrDownload /> }
         </span>
       </div>

       {
        data.tag.isOpen?(<div className=' font-semibold tag W-FULL py-2 bg-green-700  flex items-center justify-center '>
          DOWNLOAD NOW 
          </div>):null
       }
        
      </div>
       
      
    </motion.div>
  );
}

export default Card;

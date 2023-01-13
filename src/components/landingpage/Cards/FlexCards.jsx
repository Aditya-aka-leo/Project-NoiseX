import React, { useState } from 'react';

const data = [
  {
    id: 1,
    title: 'NoiseX',
    content: 'This is the content for Flexcard 1',
    child: {
      title: 'Child Flexcard 1',
      content: 'This is the content for Child Flexcard 1',
    },
  },
  {
    id: 2,
    title: 'Sound Lab',
    content: 'This is the content for Flexcard 2',
    child: {
      title: 'Child Flexcard 2',
      content: 'This is the content for Child Flexcard 2',
    },
  },
  {
    id: 3,
    title: 'Voice',
    content: 'This is the content for Flexcard 3',
    child: {
      title: 'Child Flexcard 3',
      content: 'This is the content for Child Flexcard 3',
    },
  },
  {
    id: 4,
    title: 'Melody',
    content: 'This is the content for Flexcard 4',
    child: {
      title: 'Child Flexcard 4',
      content: 'This is the content for Child Flexcard 4',
    },
  },

{
    id: 5,
    title: 'Remix',
    content: 'This is the content for Flexcard 5',
    child: {
      title: 'Child Flexcard 5',
      content: 'This is the content for Child Flexcard 5',
    },
  },
];

function FlexcardContainer() {
  const [flexcards] = useState(data);
  return (
    <div className="flexcard-container">
      {flexcards.map((item) => (
        <div key={item.id} className="flexcard">
          <h2>{item.title}</h2>
          <p>{item.content}</p>
          <div className="child-flexcard">
            <h3>{item.child.title}</h3>
            <p>{item.child.content}</p>
          </div>
        </div>
      ))}
    </div>
  );
}

export default FlexcardContainer;

import os
import glob
from pypdf import PdfReader
import openai
import numpy as np

class KnowledgeBase:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(KnowledgeBase, cls).__new__(cls)
            cls._instance.documents = []
            cls._instance.embeddings = []
            cls._instance.chunks = []
            cls._instance.initialized = False
        return cls._instance

    def initialize(self, base_dir="."):
        if self.initialized:
            return

        print("Building knowledge base from files...", flush=True)
        pdf_files = glob.glob(os.path.join(base_dir, "detailed_projects", "*.pdf"))
        md_files = glob.glob(os.path.join(base_dir, "detailed_projects", "*.md"))
        resume = os.path.join(base_dir, "RosheetaResume.pdf")
        
        all_files = pdf_files + md_files
        if os.path.exists(resume):
            all_files.append(resume)

        raw_text = ""
        for file_path in all_files:
            try:
                if file_path.endswith('.pdf'):
                    reader = PdfReader(file_path)
                    text = "\n".join([page.extract_text() for page in reader.pages])
                elif file_path.endswith('.md'):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        text = f.read()
                raw_text += f"\n\n--- Source: {os.path.basename(file_path)} ---\n\n{text}"
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

        # Simple chunking
        words = raw_text.split()
        chunk_size = 300
        overlap = 50
        
        for i in range(0, len(words), chunk_size - overlap):
            chunk = " ".join(words[i:i + chunk_size])
            if chunk:
                self.chunks.append(chunk)

        if self.chunks:
            # Generate embeddings in batches of 100
            for i in range(0, len(self.chunks), 100):
                batch = self.chunks[i:i + 100]
                response = openai.embeddings.create(
                    input=batch,
                    model="text-embedding-3-small"
                )
                self.embeddings.extend([r.embedding for r in response.data])
            
            self.embeddings = np.array(self.embeddings)
            print(f"Knowledge base initialized with {len(self.chunks)} chunks.", flush=True)
        else:
            print("No text found for knowledge base.")
            
        self.initialized = True

    def search(self, query, top_k=3):
        if not self.chunks or len(self.embeddings) == 0:
            return "No knowledge base available."
            
        response = openai.embeddings.create(
            input=query,
            model="text-embedding-3-small"
        )
        query_embedding = np.array(response.data[0].embedding)
        
        # Cosine similarity
        similarities = np.dot(self.embeddings, query_embedding) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_embedding)
        )
        
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        results = []
        for idx in top_indices:
            results.append(self.chunks[idx])
            
        return "\n\n...\n\n".join(results)

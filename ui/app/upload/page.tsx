"use client";

import { useCallback, useState } from "react";
import { useDropzone } from "react-dropzone";

export default function UploadPage() {
  const [summary, setSummary] = useState("");

  const onDrop = useCallback((acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    const formData = new FormData();
    formData.append("file", file);

    fetch("http://localhost:8000/upload", {
      method: "POST",
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => setSummary(data.summary));
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">📁 Glisser-déposer de fichiers</h2>

      <div
        {...getRootProps()}
        className="border-2 border-dashed border-gray-400 p-10 text-center rounded cursor-pointer hover:bg-gray-100"
      >
        <input {...getInputProps()} />
        {isDragActive ? (
          <p>Relâchez le fichier pour l'analyser</p>
        ) : (
          <p>Glissez-déposez un fichier ici ou cliquez pour le sélectionner</p>
        )}
      </div>

      {summary && (
        <div className="mt-6 bg-white p-4 rounded shadow">
          <h3 className="font-bold mb-2">📄 Résumé du fichier analysé :</h3>
          <pre className="whitespace-pre-wrap text-sm text-gray-800">{summary}</pre>
        </div>
      )}
    </div>
  );
}
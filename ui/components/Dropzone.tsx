"use client";
import { useCallback } from "react";
import { useDropzone } from "react-dropzone";

export function Dropzone({ onSummary }: { onSummary?: (summary: string, name: string) => void }) {
  const onDrop = useCallback((acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    const formData = new FormData();
    formData.append("file", file);

    fetch("http://localhost:8000/upload", {
      method: "POST",
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => {
        if (onSummary) {
          fetch("http://localhost:8000/memory")
            .then((res) => res.json())
            .then((data) => onSummary(data.memories.at(-1), file.name));
        }
      });
  }, [onSummary]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  return (
    <div
      {...getRootProps()}
      className={`border-2 border-dashed p-4 rounded-xl text-center cursor-pointer m-4 ${
        isDragActive ? "border-blue-400 bg-blue-50" : "border-zinc-300"
      }`}
    >
      <input {...getInputProps()} />
      <p>📁 Glissez-déposez un fichier ici pour l'analyser automatiquement</p>
    </div>
  );
}
